# 🚀 Main Entry (Internal AI Platform)

from src.application.application_service_stable import ApplicationService


def main():
    service = ApplicationService()

    print("🧠 DramaFlow Studio v4 - Internal AI Platform")
    print("Type 'exit' to quit\n")

    while True:
        query = input(">> ")
        if query.lower() == "exit":
            break

        result = service.execute_query(query)

        print("\n--- RESULT ---")
        print("Enhanced Query:", result.enhanced_query)
        print("Intent:", result.intent)
        print("Results:", result.results)
        print("---------------\n")


if __name__ == "__main__":
    main()
