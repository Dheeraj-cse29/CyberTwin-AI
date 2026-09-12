class RiskCalculator:

    @staticmethod
    def calculate_risk(
        attack_severity: int,
        detection_severity: int,
    ):
        """
        Calculate overall risk from attack and detection severity.
        Both values are expected to be between 0 and 10.
        """

        attack_severity = max(0, min(10, attack_severity))
        detection_severity = max(0, min(10, detection_severity))

        risk_score = (
            attack_severity * 0.4
            + detection_severity * 0.6
        )

        risk_score = round(risk_score, 2)

        if risk_score >= 9:
            risk_level = "CRITICAL"
        elif risk_score >= 7:
            risk_level = "HIGH"
        elif risk_score >= 4:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"

        return {
            "risk_score": risk_score,
            "risk_level": risk_level,
        }