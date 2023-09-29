import pywikibot


site = pywikibot.Site("en", "wikipedia")


while True:
    page_title = input("Enter the Wikipedia PageName: ")
    page = pywikibot.Page(site, page_title)

    if page.exists:
        page_text = page.text
        with open(page_title+".txt", "w", encoding="utf-8") as text_file:
            text_file.write(str(page_text))
    else:
        print("Entered page does not exist. Try Again")
