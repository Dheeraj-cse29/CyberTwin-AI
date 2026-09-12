from app.core.enums import AttackType


class DetectionResult:

    def __init__(
        self,
        detected: bool,
        severity: int,
        threat_level: str,
        reason: str,
    ):
        self.detected = detected
        self.severity = severity
        self.threat_level = threat_level
        self.reason = reason

    def to_dict(self):
        return {
            "detected": self.detected,
            "severity": self.severity,
            "threat_level": self.threat_level,
            "reason": self.reason,
        }


class DetectionEngine:

    @staticmethod
    def analyze_attack(attack):

        attack_type = attack.attack_type

        if attack_type == AttackType.PORT_SCAN:
            return DetectionResult(
                detected=True,
                severity=7,
                threat_level="HIGH",
                reason="Port scanning activity detected."
            )

        if attack_type == AttackType.BRUTE_FORCE:
            return DetectionResult(
                detected=True,
                severity=8,
                threat_level="HIGH",
                reason="Brute-force attack activity detected."
            )

        if attack_type == AttackType.DOS:
            return DetectionResult(
                detected=True,
                severity=10,
                threat_level="CRITICAL",
                reason="Denial-of-service activity detected."
            )

        if attack_type == AttackType.MALWARE:
            return DetectionResult(
                detected=True,
                severity=10,
                threat_level="CRITICAL",
                reason="Malware activity detected."
            )

        if attack_type == AttackType.PHISHING:
            return DetectionResult(
                detected=True,
                severity=6,
                threat_level="MEDIUM",
                reason="Phishing activity detected."
            )

        return DetectionResult(
            detected=False,
            severity=0,
            threat_level="LOW",
            reason="No known threat pattern detected."
        )