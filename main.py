import time
from agent_components import AgentThoughts, Synthesizer, InternalCritic, UncertaintyEstimator
import json

def process_insurance_claim(claim_data: dict):
    print(f"\n[1] Processing Claim: {claim_data['claim_id']} - Amount: ${claim_data['claim_amount']}")
    time.sleep(0.5)
    
    # 1. Self-Consistency Reasoning
    print("[2] Generating Independent Reasoning Paths (Self-Consistency)...")
    assessments = AgentThoughts.generate_initial_assessments(claim_data, num_paths=5)
    for a in assessments:
        print(f"    - {a}")
        time.sleep(0.2)
        
    # 2. Consensus Synthesis
    print("\n[3] Synthesizing Consensus...")
    consensus = Synthesizer.synthesize_consensus(assessments)
    print(f"    Consensus Decision: {consensus['decision']}")
    print(f"    Consistency Agreement: {consensus['consistency_confidence']*100:.0f}%")
    time.sleep(0.5)
    
    # 3. Internal Critic Review
    print("\n[4] Engaging Internal Critic Review...")
    critic_review = InternalCritic.review(claim_data, consensus, assessments)
    if critic_review["criticisms"]:
        for c in critic_review["criticisms"]:
            print(f"    ! CRITIQUE: {c}")
    else:
        print("    Critic found no major issues.")
    time.sleep(0.5)
        
    # 4. Uncertainty Estimation
    print("\n[5] Estimating Overall Uncertainty...")
    final_output = UncertaintyEstimator.estimate_uncertainty(consensus, critic_review)
    
    print("\n" + "="*50)
    print("FINAL RISK ASSESSMENT REPORT")
    print("="*50)
    print(json.dumps({
        "Claim ID": claim_data["claim_id"],
        "Initial Consensus": consensus["decision"],
        "Final Decision": final_output["final_decision"],
        "Confidence Score": f"{final_output['final_confidence_score']*100:.1f}%",
        "Requires Human Adjucator": final_output["requires_human"]
    }, indent=2))
    print("="*50 + "\n")

if __name__ == "__main__":
    ambiguous_claim = {
        "claim_id": "CLM-2026-X99",
        "claim_amount": 12500,
        "incident_type": "auto_collision",
        "time_of_incident": "late_night",
        "prior_claims_count": 2
    }
    
    process_insurance_claim(ambiguous_claim)
