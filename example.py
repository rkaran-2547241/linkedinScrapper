"""
Example usage of LinkedIn Post Scraper
"""

from linkedin_scraper import scrape_linkedin_post, LinkedInScraper
import json


def example_1_simple_scrape():
    """Example 1: Simple scrape without login"""
    print("\n=== Example 1: Simple Scrape (No Login) ===")
    
    post_url = "https://www.linkedin.com/posts/your-post-url-here"
    
    data = scrape_linkedin_post(post_url)
    
    if data:
        print("\nExtracted Data:")
        print(json.dumps(data, indent=2))


def example_2_manual_login_google():
    """Example 2: Manual login (supports Google OAuth, Microsoft, etc.)"""
    print("\n=== Example 2: Manual Login (Google OAuth Supported) ===")
    
    post_url = "https://www.linkedin.com/posts/your-post-url-here"
    
    # This will open a browser window where you can login with Google
    data = scrape_linkedin_post(
        post_url,
        manual_login=True,  # Enable manual login mode
        headless=False  # Must be False for manual login
    )
    
    if data:
        print("\nExtracted Data:")
        print(json.dumps(data, indent=2))


def example_3_with_password():
    """Example 3: Scrape with email/password login"""
    print("\n=== Example 3: Email/Password Login ===")
    
    # Replace with your credentials
    EMAIL = "your-email@example.com"
    PASSWORD = "your-password"
    
    post_url = "https://www.linkedin.com/posts/your-post-url-here"
    
    data = scrape_linkedin_post(
        post_url, 
        email=EMAIL, 
        password=PASSWORD,
        headless=False  # Set to True to run without opening browser window
    )
    
    if data:
        print("\nExtracted Data:")
        print(f"Author: {data['author']}")
        print(f"Headline: {data['author_headline']}")
        print(f"Post Text: {data['post_text']}")
        print(f"Timestamp: {data['timestamp']}")
        print(f"Likes: {data['likes']}")
        print(f"Comments: {data['comments']}")
        print(f"Images: {len(data['images'])} image(s)")


def example_4_multiple_posts():
    """Example 4: Scrape multiple posts with manual login"""
    print("\n=== Example 4: Scrape Multiple Posts (Manual Login) ===")
    
    post_urls = [
        "https://www.linkedin.com/posts/post-1",
        "https://www.linkedin.com/posts/post-2",
        "https://www.linkedin.com/posts/post-3",
    ]
    
    # Use context manager to reuse same browser session
    with LinkedInScraper(manual_login=True, headless=False) as scraper:
        for url in post_urls:
            print(f"\nScraping: {url}")
            data = scraper.scrape_post(url)
            if data:
                print(f"  Author: {data['author']}")
                print(f"  Text: {data['post_text'][:100]}...")


def example_5_save_to_file():
    """Example 5: Save scraped data to JSON file"""
    print("\n=== Example 5: Save to JSON File ===")
    
    post_url = "https://www.linkedin.com/posts/your-post-url-here"
    
    data = scrape_linkedin_post(post_url, manual_login=True)
    
    if data:
        # Save to JSON file
        with open('post_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("Data saved to post_data.json")


if __name__ == "__main__":
    print("LinkedIn Post Scraper - Examples")
    print("=" * 50)
    
    # Uncomment the example you want to run:
    
    # example_1_simple_scrape()
    # example_2_manual_login_google()  # <-- Use this for Google OAuth login
    # example_3_with_password()
    # example_4_multiple_posts()
    # example_5_save_to_file()
    
    print("\nNote: Update the post URLs in the examples before running!")
    print("For Google OAuth login, use example_2_manual_login_google() or example_4_multiple_posts()")
