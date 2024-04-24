# News Article Crawler and API

## Deployment Instructions

### Prerequisites
- Python 3.x installed
- Chrome browser installed

### Installation
1. Clone the repository:

```git clone <repository_url>```

2. Navigate to the project directory:

```cd <project_directory>```

3. Install dependencies:

```pip install -r requirements.txt```

### Running the Application standalone
1. Start the Flask API:

```python main.py```

### Running the Application with Docker
1. Build the docker image

```docker build -t <name> . ```
2. Run the docker image in a separate process

```docker run -p 5000:5000 littlebigcodecrawler```


## API Endpoints
- `/fetch_article/<url>` (GET): Fetches an article by its URL.
- `/fetch_new_articles` (GET): Initiates fetching new articles from the news website.
- `/fetch_top_authors` (GET): Retrieves the top five authors.
- `/fetch_all_articles` (GET): Retrieves all articles stored in the database.

## Production Setup

### Pipeline Setup
1. Deploy the scraping service on one or more servers using a tool like Docker or Kubernetes.
2. Configure the scraping service to crawl articles from the target website and publish messages to a message queue.
3. Deploy a message queue (e.g., RabbitMQ or Kafka) to decouple the scraping service from the database insertion process.
4. Implement a database cluster (e.g., MongoDB or Azure Cloud) to store the crawled articles with high availability and scalability.
5. Deploy an API service to expose endpoints for fetching articles and authors. The API service interacts with the database cluster.

### Limitations
- The current solution may face scalability issues due to its single-threaded approach.
- Dependency on website structure, any changes to the website's structure may break the scraping process.
- Lack of robust error handling mechanisms.

### Improvements
- Implement asynchronous processing for scraping and database insertion to improve performance and scalability.
- Enhance error handling mechanisms for graceful failure recovery.
- Implement data deduplication to avoid storing duplicate articles in the database.
- Utilize machine learning for content classification to enhance search and retrieval capabilities.

### Distributed Data Processing Framework
- Advantages:
- Scalability: Can handle large volumes of data and scale horizontally.
- Fault Tolerance: Provides fault tolerance and high availability.
- Parallel Processing: Enables parallel processing of data for faster execution.
- Disadvantages:
- Complexity: Setting up and managing a distributed framework can be complex.
- Overhead: Introduces overhead in terms of resource utilization and maintenance.
- Cost: Distributed frameworks may involve additional costs for infrastructure and maintenance.
