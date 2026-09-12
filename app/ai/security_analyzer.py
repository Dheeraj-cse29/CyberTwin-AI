from app.digital_twin.twin_engine import DigitalTwinEngine


class SecurityAnalyzer:

    @staticmethod
    def analyze(
        db,
        owner_id: int,
    ):
        state = DigitalTwinEngine.get_environment_state(
            db=db,
            owner_id=owner_id,
        )

        environment = state["environment"]
        security = state["security"]

        total_assets = environment["total_assets"]
        compromised_assets = environment["compromised_assets"]

        total_attacks = security["total_attacks"]
        total_detections = security["total_detections"]
        high_risks = security["high_risks"]
        critical_risks = security["critical_risks"]

        recommendations = []

        # Determine overall security posture
        if critical_risks > 0:
            security_status = "CRITICAL"
            recommendations.append(
                "Immediately investigate all critical risk events."
            )
        elif high_risks > 0:
            security_status = "HIGH"
            recommendations.append(
                "Investigate high-risk events and affected assets."
            )
        elif total_detections > 0:
            security_status = "MEDIUM"
            recommendations.append(
                "Review detected security events."
            )
        else:
            security_status = "LOW"
            recommendations.append(
                "Continue monitoring the environment."
            )

        # Compromised asset recommendation
        if compromised_assets > 0:
            recommendations.append(
                "Isolate and investigate compromised assets."
            )

        # Detection coverage
        if total_attacks > 0:
            detection_rate = round(
                (total_detections / total_attacks) * 100,
                2,
            )
        else:
            detection_rate = 0.0

        return {
            "security_status": security_status,
            "detection_rate": detection_rate,
            "environment": {
                "total_assets": total_assets,
                "compromised_assets": compromised_assets,
            },
            "threats": {
                "total_attacks": total_attacks,
                "total_detections": total_detections,
                "high_risks": high_risks,
                "critical_risks": critical_risks,
            },
            "recommendations": recommendations,
        }