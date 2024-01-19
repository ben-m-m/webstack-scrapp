Reddit Scraper and Database
Overview

Welcome to the Reddit Scraper and Database project! This tool allows you to efficiently scrape information from a specified subreddit on Reddit, storing the data in a structured database. Whether you're a data enthusiast, researcher, or just curious about Reddit trends, this project provides a valuable resource for extracting and analyzing post information.
Table of Contents

    Features
    Architecture
    Technologies Used
    Getting Started
        Prerequisites
        Installation
    Usage
        Fetching Posts
        Storing Posts in Database
        Retrieving Comments
    Development
        Successes
        Challenges
        Areas for Improvement
    Lessons Learned
    Demo
    Future Enhancements
    Contributing
    License

Features

    Reddit Data Scraper: Fetch top posts from a specified subreddit.
    Database Integration: Store post information in a SQLite database.
    Comment Retrieval: Retrieve and display comments based on post ID.
    User-Friendly Interface: Simple command-line interface for easy interaction.

Architecture

The project follows a client-server architecture:

    Client: Reddit API Wrapper (PRAW) for fetching posts.
    Server: SQLite Database for storing post data.

Technologies Used

    PRAW (Python Reddit API Wrapper): Interacts with the Reddit API.
    SQLite Database: Stores post information in a structured format.
    Python Programming Language: Core scripting and logic.

Getting Started
Prerequisites

    Python 3.x installed on your machine.
    Reddit API credentials (client ID, client secret, user agent).

Installation

    Clone the repository:

    bash

git clone https://github.com/ben-m-m/webstack-scrapp.git

Install project dependencies:

bash

pip install -r requirements.txt

Set up Reddit API credentials:

Obtain your Reddit API credentials (client ID, client secret, user agent) from the Reddit Developer portal.

Update praw.ini with your credentials:

ini

    [DEFAULT]
    client_id=YOUR_CLIENT_ID
    client_secret=YOUR_CLIENT_SECRET
    user_agent=YOUR_USER_AGENT

Usage
Fetching Posts

To fetch top posts from a subreddit:

bash

python3 scraper.py

Storing Posts in Database

Posts are automatically stored in the SQLite database during the fetching process.
Retrieving Comments

To retrieve and display comments based on a post ID:

bash

python3 scraper.py --comments

Development
Successes

    Successful implementation of the Reddit scraping process.
    Efficient storage of post data in an SQLite database.

Challenges

    Handling rate limits and exceptions from the Reddit API.
    Ensuring data consistency in the database during high-frequency updates.

Areas for Improvement

    Enhancing user interface and experience.
    Implementing more robust error handling and logging mechanisms.
    Scaling the application for larger datasets and increased user traffic.

Lessons Learned

    Handling API Rate Limits: Understanding and managing API rate limits proved crucial for the project's success.
    Database Schema Design: Designing an effective database schema emphasized adaptability and scalability.
    Collaboration and Communication: Effective collaboration within the team facilitated navigation through challenges.
    Balancing Functionality and Simplicity: The delicate balance between adding functionality and maintaining a simple, user-friendly application.

Demo

For a live demonstration of the Reddit Scraper and Database, refer to the presentation slides or run the project locally.
Future Enhancements

    Adding user authentication for personalized experiences.
    Implementing a web-based interface for easier interaction.

Contributing

Feel free to contribute by forking the repository, creating a new branch, making your changes, and submitting a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
