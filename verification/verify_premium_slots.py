from playwright.sync_api import sync_playwright
import time

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:5000/")
        page.wait_for_timeout(3000)
        
        # Dismiss Popups
        if page.get_by_text("CLAIM NOW").is_visible(): 
            page.get_by_text("CLAIM NOW").click()
            page.wait_for_timeout(500)
        if page.get_by_text("Reward Claimed").is_visible(): 
            page.locator("div[role='dialog'] button").last.click()
            page.wait_for_timeout(500)
        if page.get_by_text("Terms & Conditions").is_visible(): 
            page.get_by_role("button", name="I Agree & Continue").click()
            page.wait_for_timeout(500)
        if page.get_by_text("Unlock Smart Learning").is_visible(): 
            page.locator("div.fixed button").last.click()
            page.wait_for_timeout(500)
        if page.get_by_text("Resume Learning").is_visible(): 
            page.get_by_text("Resume Learning").click()
            page.wait_for_timeout(500)

        # Admin Dashboard Check
        if page.get_by_text("Admin Console").is_visible():
            print("On Admin Dashboard")
            
            # Navigate to PDF Content
            print("Clicking PDF/AI Notes...")
            page.get_by_text("PDF/AI Notes").first.click()
            page.wait_for_timeout(2000)
            
            # Select Subject Science
            print("Selecting Subject...")
            page.get_by_role("button", name="Science").first.click()
            page.wait_for_timeout(1000)
            
            # Click Manage All Content on first chapter
            print("Managing Content...")
            page.get_by_text("Manage All Content").first.click()
            page.wait_for_timeout(2000)
            
            # Scroll to find Premium Notes Collection
            print("Scrolling...")
            page.mouse.wheel(0, 1500) # Scroll down enough
            page.wait_for_timeout(1000)
            
            # Check for Header
            if page.get_by_text("Premium Notes Collection").is_visible():
                print("✅ Premium Notes Collection Section Found!")
                # Take screenshot of the section
                page.screenshot(path="verification/premium_slots.png")
            else:
                print("❌ Premium Notes Collection Section NOT Found!")
                page.screenshot(path="verification/failed_slots.png")
                
        else:
            print("Not on Admin Dashboard")
            page.screenshot(path="verification/not_admin.png")
            
        browser.close()

if __name__ == "__main__":
    verify()
