from client import EnterpriseAiAgentControlPlaneGovernorClient

def main():
    client = EnterpriseAiAgentControlPlaneGovernorClient()
    res = client.govern_agent_request({"agent_id": "finance_bot_01", "tokens": 5000})
    print(f"Status: {res['governance_status']}")
    print(f"Routed Model: {res['routed_model']}")

if __name__ == "__main__":
    main()
