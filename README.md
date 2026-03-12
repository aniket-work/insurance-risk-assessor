# Autonomous Insurance Claims Risk Assessor

> **Risk-Aware AI Agent with Internal Critic, Self-Consistency Reasoning, & Uncertainty Estimation**

![Risk Assessor Action](https://raw.githubusercontent.com/aniket-work/insurance-risk-assessor/main/images/title-animation.gif)

## Overview

Applying autonomous agents to high-stakes environments requires robust self-correction mechanisms. This project demonstrates an experimental **Risk-Aware AI Agent** designed for the insurance sector to evaluate ambiguous auto collision claims.

By blending multiple reasoning paths with an adversarial critic model, the system evaluates subjective data (like the claimant's reporting timeline and amount vs. historical trends) to assess fraud risk and produce confidence scores that gate human intervention.

## 🏗 System Architecture

![Architecture](https://raw.githubusercontent.com/aniket-work/insurance-risk-assessor/main/images/architecture_diagram.png)

### Key Agent Components
1. **Self-Consistency Engine**: Queries language models across dynamically rotated focuses (e.g., *Medical History*, *Time of Incident*). Simulates multi-agent consensus vs. relying on a zero-shot result.
2. **Internal Critic**: A completely distinct review agent programmed specifically to look for edge cases, missing documentation points, or statistical outliers the consensus team might have missed. 
3. **Uncertainty Estimator**: Calculates a mathematical confidence penalty based on initial disagreement and the critic's severity. If confidence dips below 70%, or a severe exception is found, the agent intentionally halts the workflow and escalates to a human adjudicator.

## 🚀 The Execution Flow

![Process Flow](https://raw.githubusercontent.com/aniket-work/insurance-risk-assessor/main/images/flow_diagram.png)

The workflow consists of four steps. Let's trace it given a mocked auto collision claim:

1. **Extract Features**: Loads claimant history, incident time ("late_night"), and claim quantity ($12,500).
2. **Path Generation**: We spin up `N=5` parallel virtual thinking tracks. Each calculates risk based on a different focus area.
3. **Review & Flag**: The critic agent flags the high value without secondary checks, while the uncertainty engine penalizes the final confidence score down to 15.0%.
4. **Conclusion**: The claim is safely routed to the human team instead of auto-approval.

[Read the full deep-dive article on Dev.to](https://dev.to/aniket/how-i-automated-insurance-risk-analysis-using-multi-agent-reasoning-and-internal-critics)

## 🛠 Running the Simulation

```bash
# Clone the repository
git clone https://github.com/aniket-work/insurance-risk-assessor.git
cd insurance-risk-assessor

# Install dependencies
python3 -m venv venv
source venv/bin/activate

# Execute the agent simulation
python main.py
```

### Example Simulation Output:
```text
[1] Processing Claim: CLM-2026-X99 - Amount: $12500
[2] Generating Independent Reasoning Paths (Self-Consistency)...
    - Path 1: Focusing on medical_history. Calculated Risk Score: 0.61. Recommendation: FLAG FOR MANUAL REVIEW.
    - Path 2: Focusing on time_of_reporting. Calculated Risk Score: 0.82. Recommendation: FLAG FOR MANUAL REVIEW.
    - Path 3: Focusing on claim_amount. Calculated Risk Score: 0.45. Recommendation: AUTO-APPROVE.
    - Path 4: Focusing on time_of_reporting. Calculated Risk Score: 0.81. Recommendation: FLAG FOR MANUAL REVIEW.
    - Path 5: Focusing on provider_reputation. Calculated Risk Score: 0.39. Recommendation: AUTO-APPROVE.

[3] Synthesizing Consensus...
    Consensus Decision: FLAG FOR MANUAL REVIEW
    Consistency Agreement: 60%

[4] Engaging Internal Critic Review...
    ! CRITIQUE: Critic Note: Auto-approving high-value claim ($10k+) without secondary documentation check.
    ! CRITIQUE: Critic Note: Disagreement in initial reasoning paths indicates underlying ambiguity.

[5] Estimating Overall Uncertainty...

==================================================
FINAL RISK ASSESSMENT REPORT
==================================================
{
  "Claim ID": "CLM-2026-X99",
  "Initial Consensus": "FLAG FOR MANUAL REVIEW",
  "Final Decision": "FLAG FOR MANUAL REVIEW",
  "Confidence Score": "15.0%",
  "Requires Human Adjucator": true
}
==================================================
```

## Agent Communication Protocol

![Sequence](https://raw.githubusercontent.com/aniket/insurance-risk-assessor/main/images/sequence_diagram.png)

## ⚠️ Disclaimer

The views and opinions expressed here are solely my own and do not represent the views, positions, or opinions of my employer or any organization I am affiliated with. The content is based on my personal experience and experimentation and may be incomplete or incorrect. Any errors or misinterpretations are unintentional, and I apologize in advance if any statements are misunderstood or misrepresented.
