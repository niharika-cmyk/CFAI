# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online edito
from collections import deque
from dataclasses import dataclass
import heapq

# --------------------------------
# CO1 : State Representation
# --------------------------------
@dataclass
class Ticket:
    ticket_id: str
    issue_type: str
    priority: str
    department: str


# --------------------------------
# CO1 : PEAS Model
# --------------------------------
class PEAS:
    performance = "Fast Ticket Resolution"
    environment = "Helpdesk Support System"
    actuators = "Ticket Assignment"
    sensors = "User Queries and Ticket Data"


# --------------------------------
# CO2 : Search Algorithms
# --------------------------------
class SearchAlgorithms:

    def bfs(self, graph, start):

        visited = set()
        queue = deque([start])

        print("\nBFS Traversal:")

        while queue:

            node = queue.popleft()

            if node not in visited:

                print(node, end=" ")
                visited.add(node)

                for neighbor in graph[node]:
                    queue.append(neighbor)

        print()

    def dfs(self, graph, start, visited=None):

        if visited is None:
            visited = set()
            print("\nDFS Traversal:")

        visited.add(start)

        print(start, end=" ")

        for neighbor in graph[start]:

            if neighbor not in visited:
                self.dfs(graph, neighbor, visited)

    def ucs(self, graph, start, goal):

        pq = [(0, start)]
        visited = set()

        while pq:

            cost, node = heapq.heappop(pq)

            if node == goal:

                print(f"\nUCS Minimum Cost from {start} to {goal}: {cost}")
                return

            if node not in visited:

                visited.add(node)

                for neighbor, weight in graph[node]:

                    heapq.heappush(
                        pq,
                        (cost + weight, neighbor)
                    )


# --------------------------------
# CO3 : Constraint Satisfaction
# --------------------------------
class CSPValidator:

    def validate(self, ticket):

        if ticket.ticket_id == "":
            print("\nInvalid Ticket ID")
            return False

        if ticket.priority not in ["Low", "Medium", "High"]:
            print("\nPriority must be Low, Medium or High")
            return False

        if ticket.department == "":
            print("\nDepartment cannot be empty")
            return False

        return True


# --------------------------------
# CO4 : Utility Function
# --------------------------------
class UtilityFunction:

    def calculate(self, priority):

        if priority == "High":
            return 10

        elif priority == "Medium":
            return 5

        else:
            return 2


# --------------------------------
# CO5 : Bayesian Reasoning
# --------------------------------
class BayesianReasoning:

    def bayes_rule(self, prior, likelihood, evidence):

        return (prior * likelihood) / evidence


# --------------------------------
# CO6 : Hybrid AI System
# --------------------------------
class AutomatedHelpdeskReasoner:

    def __init__(self):

        self.search = SearchAlgorithms()
        self.csp = CSPValidator()
        self.utility = UtilityFunction()
        self.bayes = BayesianReasoning()

    def show_title(self):

        print("=" * 60)
        print("        AUTOMATED HELPDESK REASONER")
        print("=" * 60)

    def show_menu(self):

        print("\n1. Create Ticket")
        print("2. Run BFS and DFS")
        print("3. Run UCS")
        print("4. Bayesian Analysis")
        print("5. Exit")

    def create_ticket(self):

        print("\nEnter Ticket Details")

        ticket_id = input("Ticket ID       : ")
        issue_type = input("Issue Type      : ")
        priority = input("Priority (Low/Medium/High): ")
        department = input("Department      : ")

        ticket = Ticket(
            ticket_id,
            issue_type,
            priority,
            department
        )

        if not self.csp.validate(ticket):
            return

        utility_score = self.utility.calculate(priority)

        print("\nTicket Information")
        print("-" * 40)
        print("Ticket ID   :", ticket.ticket_id)
        print("Issue Type  :", ticket.issue_type)
        print("Priority    :", ticket.priority)
        print("Department  :", ticket.department)

        print("\nUtility Score :", utility_score)

        if utility_score >= 10:
            print("Recommendation : Immediate Escalation")

        elif utility_score >= 5:
            print("Recommendation : Assign to Support Team")

        else:
            print("Recommendation : Normal Queue Processing")

    def run_bfs_dfs(self):

        graph = {
            "Helpdesk": ["Technical", "Billing", "Network"],
            "Technical": ["Software", "Hardware"],
            "Billing": [],
            "Network": [],
            "Software": [],
            "Hardware": []
        }

        self.search.bfs(graph, "Helpdesk")
        self.search.dfs(graph, "Helpdesk")

        print()

    def run_ucs(self):

        graph = {
            "Helpdesk": [("Technical", 2), ("Billing", 3)],
            "Technical": [("Software", 1)],
            "Billing": [("Network", 2)],
            "Software": [],
            "Network": []
        }

        self.search.ucs(
            graph,
            "Helpdesk",
            "Software"
        )

    def run_bayesian_analysis(self):

        prior = 0.6
        likelihood = 0.8
        evidence = 0.9

        result = self.bayes.bayes_rule(
            prior,
            likelihood,
            evidence
        )

        print("\nBayesian Analysis")
        print("Escalation Probability :", round(result, 2))

    def run(self):

        while True:

            self.show_title()
            self.show_menu()

            choice = input("\nEnter Choice : ")

            if choice == "1":

                self.create_ticket()

            elif choice == "2":

                self.run_bfs_dfs()

            elif choice == "3":

                self.run_ucs()

            elif choice == "4":

                self.run_bayesian_analysis()

            elif choice == "5":

                print("\nThank You")
                break

            else:

                print("\nInvalid Choice")


# --------------------------------
# Main Function
# --------------------------------
if __name__ == "__main__":

    system = AutomatedHelpdeskReasoner()
    system.run()
