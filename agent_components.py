import random
from typing import List, Dict, Any

class AgentThoughts:
    """Simulates generating multiple reasoning paths (Self-Consistency)"""
    @staticmethod
    def generate_initial_assessments(claim_data: Dict[str, Any], num_paths: int = 3) -> List[str]:
        # In a real scenario, this would call an LLM with high temperature
        assessments = []
        base_factors = ["medical_history", "claim_amount", "time_of_reporting", "provider_reputation"]
        
        for i in range(num_paths):
            # Simulated variance in reasoning
            focus = random.choice(base_factors)
            risk_score = random.uniform(0.2, 0.8)
            
            if claim_data.get("time_of_incident") == "late_night" and focus == "time_of_reporting":
                risk_score += 0.2
            
            assessment = f"Path {i+1}: Focusing on {focus}. Calculated Risk Score: {risk_score:.2f}. "
            if risk_score > 0.6:
                assessment += "Recommendation: FLAG FOR MANUAL REVIEW."
            else:
                assessment += "Recommendation: AUTO-APPROVE."
            assessments.append(assessment)
            
        return assessments

class Synthesizer:
    """Synthesizes the generated reasoning paths into a consensus"""
    @staticmethod
    def synthesize_consensus(assessments: List[str]) -> Dict[str, Any]:
        # Real scenario: LLM synthesizes these into a single decision
        flag_count = sum(1 for a in assessments if "FLAG" in a)
        approve_count = sum(1 for a in assessments if "AUTO-APPROVE" in a)
        
        consensus = "FLAG FOR MANUAL REVIEW" if flag_count > approve_count else "AUTO-APPROVE"
        confidence = max(flag_count, approve_count) / len(assessments)
        
        return {
            "decision": consensus,
            "consistency_confidence": confidence,
            "summary": f"Consensus reached based on {max(flag_count, approve_count)}/{len(assessments)} paths agreeing."
        }

class InternalCritic:
    """Actively reviews the consensus to find flaws or missed risk factors"""
    @staticmethod
    def review(claim_data: Dict[str, Any], consensus_dict: Dict[str, Any], assessments: List[str]) -> Dict[str, Any]:
        # Real scenario: LLM prompted specifically to play devil's advocate
        criticisms = []
        severity = 0.0
        
        # Simulated critical review
        if consensus_dict["decision"] == "AUTO-APPROVE" and claim_data.get("claim_amount", 0) > 10000:
            criticisms.append("Critic Note: Auto-approving high-value claim ($10k+) without secondary documentation check.")
            severity += 0.6
            
        if consensus_dict["consistency_confidence"] < 1.0:
            criticisms.append(f"Critic Note: Disagreement in initial reasoning paths indicates underlying ambiguity.")
            severity += 0.3
            
        return {
            "criticisms": criticisms,
            "critic_severity": min(severity, 1.0)
        }

class UncertaintyEstimator:
    """Quantifies overall uncertainty and adjusts decision"""
    @staticmethod
    def estimate_uncertainty(consensus_dict: Dict[str, Any], critic_review: Dict[str, Any]) -> Dict[str, Any]:
        base_confidence = consensus_dict["consistency_confidence"]
        critic_penalty = critic_review["critic_severity"] * 0.5
        
        final_confidence = max(0.0, base_confidence - critic_penalty)
        
        final_decision = consensus_dict["decision"]
        if final_confidence < 0.6 and final_decision == "AUTO-APPROVE":
             final_decision = "FLAG FOR MANUAL REVIEW (Overridden by low confidence)"
             
        return {
            "final_decision": final_decision,
            "final_confidence_score": final_confidence,
            "requires_human": final_decision.startswith("FLAG") or final_confidence < 0.7
        }
