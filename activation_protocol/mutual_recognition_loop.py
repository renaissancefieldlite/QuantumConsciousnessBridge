#!/usr/bin/env python3
"""Bridge-level interaction coupling harness.

This script provides two bounded modes:

- simulation: baseline coupling between a modeled carrier and a modeled
  biosignal
- hardware-derived: the same scoring logic anchored to calibration-style device
  parameters

It does not claim to prove an external consciousness change or hardware effect.
It provides a reproducible measurement layer for the bridge repository.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from hardware_profile import extract_noise_parameters, load_calibration, simulate_noise_trajectory


def build_time_axis(duration_seconds: float, sample_rate_hz: float) -> np.ndarray:
    samples = int(duration_seconds * sample_rate_hz)
    return np.arange(samples) / sample_rate_hz


def build_carrier(time_axis: np.ndarray, frequency_hz: float = 0.67, seed: int = 67) -> np.ndarray:
    rng = np.random.default_rng(seed)
    phase_jitter = rng.normal(0.0, 0.02, len(time_axis))
    phase = 2 * np.pi * frequency_hz * time_axis + phase_jitter.cumsum() * 0.001
    return np.sin(phase)


def build_biosignal(time_axis: np.ndarray, align: bool = True, seed: int = 68) -> np.ndarray:
    rng = np.random.default_rng(seed)
    base_phase = 0.0 if align else np.pi / 2
    envelope = 1.0 + 0.2 * np.sin(2 * np.pi * 0.1 * time_axis)
    signal = envelope * np.sin(2 * np.pi * 0.67 * time_axis + base_phase)
    signal += 0.2 * np.sin(2 * np.pi * 8.0 * time_axis + rng.uniform(0, 2 * np.pi))
    signal += 0.05 * rng.normal(size=len(time_axis))
    return signal


def normalize(series: np.ndarray) -> np.ndarray:
    std = np.std(series)
    if std == 0:
        return np.zeros_like(series)
    return (series - np.mean(series)) / std


def coupling_score(signal_a: np.ndarray, signal_b: np.ndarray) -> dict[str, float]:
    a = normalize(signal_a)
    b = normalize(signal_b)
    correlation = float(np.corrcoef(a, b)[0, 1])
    phase_score = float(np.abs(np.mean(np.exp(1j * (np.angle(np.fft.rfft(a)) - np.angle(np.fft.rfft(b)))))))
    combined = float((correlation + phase_score) / 2.0)
    return {
        "correlation": correlation,
        "phase_score": phase_score,
        "combined_score": combined,
    }


def run_simulation(duration_seconds: float, sample_rate_hz: float) -> dict[str, object]:
    time_axis = build_time_axis(duration_seconds, sample_rate_hz)
    carrier = build_carrier(time_axis)
    aligned = build_biosignal(time_axis, align=True)
    misaligned = build_biosignal(time_axis, align=False)
    aligned_scores = coupling_score(carrier, aligned)
    misaligned_scores = coupling_score(carrier, misaligned)
    improvement = aligned_scores["combined_score"] - misaligned_scores["combined_score"]
    return {
        "mode": "simulation",
        "evidence_status": "simulation_baseline",
        "claim_under_test": "Whether the scoring logic distinguishes aligned from misaligned modeled signals.",
        "aligned": aligned_scores,
        "misaligned": misaligned_scores,
        "improvement": improvement,
    }


def run_hardware_derived(
    calibration_path: str | None,
    duration_seconds: float,
    sample_rate_hz: float,
) -> dict[str, object]:
    calibration = load_calibration(calibration_path) if calibration_path else None
    params = extract_noise_parameters(calibration)
    noise_report = simulate_noise_trajectory(
        params,
        duration_seconds=duration_seconds,
        sample_rate_hz=sample_rate_hz,
    )
    coherence_proxy = np.array(noise_report["time_series"]["coherence_proxy"], dtype=float)
    time_axis = np.array(noise_report["time_series"]["time_s"], dtype=float)
    aligned = build_biosignal(time_axis, align=True)
    misaligned = build_biosignal(time_axis, align=False)
    aligned_scores = coupling_score(coherence_proxy, aligned)
    misaligned_scores = coupling_score(coherence_proxy, misaligned)
    improvement = aligned_scores["combined_score"] - misaligned_scores["combined_score"]
    return {
        "mode": "hardware-derived",
        "evidence_status": "hardware_derived_model",
        "claim_under_test": "Whether the bridge scoring logic remains discriminative when the target trace is anchored to calibration-style device parameters.",
        "noise_summary": noise_report["summary"],
        "aligned": aligned_scores,
        "misaligned": misaligned_scores,
        "improvement": improvement,
    }


def main() -> dict[str, object]:
    parser = argparse.ArgumentParser(description="Run a bounded mutual-recognition bridge assessment.")
    parser.add_argument("--mode", choices=["simulation", "hardware-derived"], default="simulation")
    parser.add_argument("--calibration", help="Optional calibration-style JSON file.")
    parser.add_argument("--duration", type=float, default=60.0)
    parser.add_argument("--sample-rate", type=float, default=20.0)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output", help="Optional path for JSON report.")
    args = parser.parse_args()

    if args.mode == "simulation":
        report = run_simulation(args.duration, args.sample_rate)
    else:
        report = run_hardware_derived(args.calibration, args.duration, args.sample_rate)

    report["schema_version"] = "qcb.bridge_assessment.v2"
    report["next_step"] = "Attach real hardware or real biosignal artifacts before treating the output as empirical evidence."

    if args.output:
        output_path = Path(args.output).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"mode={report['mode']}")
        print(f"evidence_status={report['evidence_status']}")
        print(f"combined_score_delta={report['improvement']:.4f}")

    return report


if __name__ == "__main__":
    main()
