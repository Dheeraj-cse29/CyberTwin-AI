from app.core.enums import AttackType


class MitreMapper:

    ATTACK_MAPPINGS = {
        AttackType.PORT_SCAN: {
            "technique_id": "T1046",
            "technique_name": "Network Service Scanning",
            "tactic": "Discovery",
        },

        AttackType.BRUTE_FORCE: {
            "technique_id": "T1110",
            "technique_name": "Brute Force",
            "tactic": "Credential Access",
        },

        AttackType.DOS: {
            "technique_id": "T1498",
            "technique_name": "Network Denial of Service",
            "tactic": "Impact",
        },

        AttackType.MALWARE: {
            "technique_id": "T1204",
            "technique_name": "User Execution",
            "tactic": "Execution",
        },

        AttackType.PHISHING: {
            "technique_id": "T1566",
            "technique_name": "Phishing",
            "tactic": "Initial Access",
        },
    }

    @staticmethod
    def map_attack(attack_type: AttackType):

        return MitreMapper.ATTACK_MAPPINGS.get(
            attack_type,
            {
                "technique_id": "UNKNOWN",
                "technique_name": "Unknown Technique",
                "tactic": "Unknown",
            },
        )