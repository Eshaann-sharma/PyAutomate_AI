from modules.rpa import scraper, desktop_bot, ocr_engine

def run_scraper():
    print("Running Web Scraper")
    data = scraper.scrape_books()
    scraper.save_to_csv(data)
    print(f"!!!!Scraped {len(data)} books.\n")

def run_desktop_bot():
    print("Running Desktop Bot")
    desktop_bot.open_application("notepad.exe")
    desktop_bot.type_text("Hello from PyAutomate AI")
    print("!!!Desktop automation complete.\n")

def run_ocr():
    print("Running OCR")
    result = ocr_engine.extract_text_from_image("sample_image.png")
    print("!!!OCR Result:\n", result)

if __name__ == "__main__":
    print("Starting PyAutomate RPA Engine\n")
    run_scraper()
    run_desktop_bot()
    run_ocr()
    print("\n!!!All RPA modules executed.")
