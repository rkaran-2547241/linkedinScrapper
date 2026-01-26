"""
Example usage of LinkedIn Profile Scraper
Extracts experience, education, certifications, skills, and more from LinkedIn profiles
"""

from linkedin_scraper import scrape_linkedin_profile, LinkedInScraper
import json


def example_1_simple_profile_scrape():
    """Example 1: Simple profile scrape with manual login"""
    print("\n=== Example 1: Scrape LinkedIn Profile ===")
    
    profile_url = "https://www.linkedin.com/in/username/"
    
    # Manual login recommended for full profile access
    data = scrape_linkedin_profile(profile_url, manual_login=True)
    
    if data:
        print("\n✓ Profile Data Extracted:")
        print(f"Name: {data['name']}")
        print(f"Headline: {data['headline']}")
        print(f"Location: {data['location']}")
        print(f"Current Company: {data['current_company']}")
        print(f"\nExperience Entries: {len(data['experience'])}")
        print(f"Education Entries: {len(data['education'])}")
        print(f"Certifications: {len(data['certifications'])}")
        print(f"Skills: {len(data['skills'])}")


def example_2_extract_experience():
    """Example 2: Focus on extracting work experience"""
    print("\n=== Example 2: Extract Work Experience ===")
    
    profile_url = "https://www.linkedin.com/in/username/"
    
    data = scrape_linkedin_profile(profile_url, manual_login=True)
    
    if data and data['experience']:
        print("\n📊 Work Experience:")
        print("=" * 60)
        
        for i, exp in enumerate(data['experience'], 1):
            print(f"\n{i}. {exp.get('title', 'N/A')}")
            print(f"   Company: {exp.get('company', 'N/A')}")
            print(f"   Duration: {exp.get('duration', 'N/A')}")
            print(f"   Location: {exp.get('location', 'N/A')}")
            if 'description' in exp:
                print(f"   Description: {exp['description'][:100]}...")


def example_3_extract_education_certs():
    """Example 3: Extract education and certifications"""
    print("\n=== Example 3: Education & Certifications ===")
    
    profile_url = "https://www.linkedin.com/in/username/"
    
    data = scrape_linkedin_profile(profile_url, manual_login=True)
    
    if data:
        # Education
        if data['education']:
            print("\n🎓 Education:")
            print("=" * 60)
            for edu in data['education']:
                print(f"• {edu.get('school', 'N/A')}")
                print(f"  {edu.get('degree', 'N/A')}")
                print(f"  {edu.get('duration', 'N/A')}\n")
        
        # Certifications
        if data['certifications']:
            print("\n📜 Certifications:")
            print("=" * 60)
            for cert in data['certifications']:
                print(f"• {cert.get('name', 'N/A')}")
                print(f"  Issuer: {cert.get('issuer', 'N/A')}")
                print(f"  Date: {cert.get('date', 'N/A')}\n")


def example_4_multiple_profiles():
    """Example 4: Scrape multiple profiles"""
    print("\n=== Example 4: Scrape Multiple Profiles ===")
    
    profile_urls = [
        "https://www.linkedin.com/in/profile1/",
        "https://www.linkedin.com/in/profile2/",
        "https://www.linkedin.com/in/profile3/",
    ]
    
    all_profiles = []
    
    # Use context manager to reuse browser session
    with LinkedInScraper(manual_login=True, headless=False) as scraper:
        for url in profile_urls:
            print(f"\nScraping: {url}")
            data = scraper.scrape_profile(url)
            
            if data:
                all_profiles.append(data)
                print(f"  ✓ {data['name']} - {data['headline']}")
    
    print(f"\n✓ Successfully scraped {len(all_profiles)} profiles")
    return all_profiles


def example_5_save_to_file():
    """Example 5: Scrape profile and save to JSON"""
    print("\n=== Example 5: Save Profile Data to JSON ===")
    
    profile_url = "https://www.linkedin.com/in/username/"
    
    data = scrape_linkedin_profile(profile_url, manual_login=True)
    
    if data:
        # Create filename from profile name
        filename = f"profile_{data['name'].replace(' ', '_')}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Profile data saved to {filename}")
        print(f"\nProfile Summary:")
        print(f"  Name: {data['name']}")
        print(f"  Current Role: {data['headline']}")
        print(f"  Experience: {len(data['experience'])} positions")
        print(f"  Education: {len(data['education'])} institutions")
        print(f"  Skills: {len(data['skills'])} skills")


def example_6_extract_skills():
    """Example 6: Focus on extracting skills"""
    print("\n=== Example 6: Extract Skills ===")
    
    profile_url = "https://www.linkedin.com/in/username/"
    
    data = scrape_linkedin_profile(profile_url, manual_login=True)
    
    if data and data['skills']:
        print(f"\n💡 Skills ({len(data['skills'])} total):")
        print("=" * 60)
        
        for i, skill in enumerate(data['skills'], 1):
            print(f"{i}. {skill}")


def example_7_compare_profiles():
    """Example 7: Compare two profiles side by side"""
    print("\n=== Example 7: Compare Two Profiles ===")
    
    profile1_url = "https://www.linkedin.com/in/profile1/"
    profile2_url = "https://www.linkedin.com/in/profile2/"
    
    with LinkedInScraper(manual_login=True) as scraper:
        profile1 = scraper.scrape_profile(profile1_url)
        profile2 = scraper.scrape_profile(profile2_url)
    
    if profile1 and profile2:
        print("\n📊 Profile Comparison:")
        print("=" * 80)
        print(f"{'Metric':<25} {'Profile 1':<25} {'Profile 2':<25}")
        print("-" * 80)
        print(f"{'Name':<25} {profile1['name']:<25} {profile2['name']:<25}")
        print(f"{'Current Company':<25} {profile1['current_company']:<25} {profile2['current_company']:<25}")
        print(f"{'Experience Count':<25} {len(profile1['experience']):<25} {len(profile2['experience']):<25}")
        print(f"{'Education Count':<25} {len(profile1['education']):<25} {len(profile2['education']):<25}")
        print(f"{'Certifications':<25} {len(profile1['certifications']):<25} {len(profile2['certifications']):<25}")
        print(f"{'Skills Count':<25} {len(profile1['skills']):<25} {len(profile2['skills']):<25}")


if __name__ == "__main__":
    print("LinkedIn Profile Scraper - Examples")
    print("=" * 60)
    print("\nAvailable Examples:")
    print("1. Simple profile scrape")
    print("2. Extract work experience")
    print("3. Extract education & certifications")
    print("4. Scrape multiple profiles")
    print("5. Save profile to JSON file")
    print("6. Extract skills")
    print("7. Compare two profiles")
    
    choice = input("\nSelect example to run (1-7): ").strip()
    
    examples = {
        '1': example_1_simple_profile_scrape,
        '2': example_2_extract_experience,
        '3': example_3_extract_education_certs,
        '4': example_4_multiple_profiles,
        '5': example_5_save_to_file,
        '6': example_6_extract_skills,
        '7': example_7_compare_profiles
    }
    
    if choice in examples:
        examples[choice]()
    else:
        print("Invalid choice!")
    
    print("\nNote: Replace 'username' in URLs with actual LinkedIn usernames before running!")
