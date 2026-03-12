import base64
import requests
import os

def generate():
    os.makedirs("images", exist_ok=True)
    
    diagrams = {
        "title": """graph LR
    subgraph "Intelligent Risks Assessor"
        A[Incoming Claim] --> B(Self-Consistency Reasoning)
        B --> C{Consensus Synthesis}
        C --> D((Internal Critic))
        D -. "Adversarial Review" .-> C
        C --> E[Uncertainty Estimation]
        E --> F[Final Decision]
        E -. "Low Confidence" .-> G[Human Expert]
    end
    style A fill:#4F46E5,color:#fff,stroke-width:0px
    style C fill:#10B981,color:#fff,stroke-width:0px
    style D fill:#EF4444,color:#fff,stroke-width:0px
    style F fill:#F59E0B,color:#fff,stroke-width:0px
    """,
        
        "architecture": """graph TB
    Client((Claim System)) --> API[API Gateway]
    API --> Agent[Risk-Aware Agent]
    
    subgraph "Agent Architecture"
        Agent --> SC[Self-Consistency Engine]
        SC --> LLM1[LLM - Path 1]
        SC --> LLM2[LLM - Path 2]
        SC --> LLMn[LLM - Path n]
        
        LLM1 & LLM2 & LLMn --> SYN[Consensus Synthesizer]
        SYN --> CRITIC[Internal Critic Agent]
        CRITIC -- "Feedback Loop" --> SYN
        
        SYN --> UNCERT[Uncertainty Estimator]
    end
    
    UNCERT --> Result[Decision Output]
    Result --> Client
    """,
        
        "sequence": """sequenceDiagram
    participant System as Claims System
    participant Orchestrator
    participant Agents as LLM Reasoners
    participant Critic as Internal Critic
    
    System->>Orchestrator: Submit Claim #99X
    Orchestrator->>Agents: Generate multiple assessments (N=5)
    Agents-->>Orchestrator: Return 5 unique reasoning paths
    Orchestrator->>Orchestrator: Synthesize consensus
    Orchestrator->>Critic: Review consensus & inputs
    Critic-->>Orchestrator: Return vulnerabilities/severity
    Orchestrator->>Orchestrator: Calculate Uncertainty Score
    alt Confidence > 80%
        Orchestrator-->>System: Auto-Approve Claim
    else Confidence <= 80%
        Orchestrator-->>System: Flag for Manual Review
    end
    """,
        
        "flow": """graph LR
    A[Start Claim] --> B[Generate Assessments]
    B --> C[Synthesize Consensus]
    C --> D[Critic Review]
    D --> E[Estimate Uncertainty]
    E --> F[Output Final Decision]
    """
    }

    for name, code in diagrams.items():
        print(f"Generating {name}_diagram.png...")
        encoded = base64.b64encode(code.encode('utf-8')).decode('utf-8')
        url = f"https://mermaid.ink/img/{encoded}?bgColor=FFFFFF"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            file_path = f"images/{name}_diagram.png"
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Successfully saved {file_path}")
        except Exception as e:
            print(f"Error generating {name}: {e}")
            raise

if __name__ == "__main__":
    generate()
