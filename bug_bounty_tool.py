import logging
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from synthetic_dataset import data, labels

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AIBugDetector:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression()
        self.trained = False

    def train(self, data, labels):
        X = self.vectorizer.fit_transform(data)
        self.model.fit(X, labels)
        self.trained = True
        logging.info("AI model trained for bug detection.")

    def predict(self, code_snippet):
        if not self.trained:
            logging.warning("AI model is not trained yet.")
            return []
        X = self.vectorizer.transform([code_snippet])
        prediction = self.model.predict(X)
        return prediction


# Preprocess the data and train the AI model
ai_detector = AIBugDetector()
ai_detector.train(data, labels)

class BugBountyTool:
    def __init__(self):
        self.bugs = []
        self.ai_detector = ai_detector

    def log_bug(self, title, description):
        bug = {
            'title': title,
            'description': description,
            'status': 'open'
        }
        self.bugs.append(bug)
        logging.info(f"Bug logged: {title}")

    def ai_log_bug(self, code_snippet):
        prediction = self.ai_detector.predict(code_snippet)
        if prediction:
            self.log_bug("AI Detected Bug", code_snippet)

    def update_bug_status(self, title, status):
        for bug in self.bugs:
            if bug['title'] == title:
                bug['status'] = status
                logging.info(f"Bug '{title}' status updated to {status}")
                return
        logging.warning(f"Bug '{title}' not found")

    def generate_report(self):
        logging.info("Generating Bug Report:")
        for bug in self.bugs:
            logging.info(f"Title: {bug['title']}, Status: {bug['status']}")


def main():
    parser = argparse.ArgumentParser(description='Bug Bounty Tool')
    parser.add_argument('--log', nargs=2, metavar=('title', 'description'), help='Log a new bug')
    parser.add_argument('--update', nargs=2, metavar=('title', 'status'), help='Update the status of a bug')
    parser.add_argument('--report', action='store_true', help='Generate a bug report')
    parser.add_argument('--ai-log', metavar='code_snippet', help='Log a bug using AI detection')
    args = parser.parse_args()

    tool = BugBountyTool()

    if args.log:
        tool.log_bug(args.log[0], args.log[1])
    if args.update:
        tool.update_bug_status(args.update[0], args.update[1])
    if args.report:
        tool.generate_report()
    if args.ai_log:
        tool.ai_log_bug(args.ai_log)


if __name__ == "__main__":
    main()
