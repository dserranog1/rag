from datetime import datetime
from pathlib import Path

import scrapy


class DegreesSpider(scrapy.Spider):
    name = "degrees"

    def start_requests(self):
        urls = [
            "https://manizales.unal.edu.co/menu/programas-academicos/carreras/matematicas/",
            "https://manizales.unal.edu.co/menu/programas-academicos/carreras/administracion-de-empresas/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/carreras/administracion-de-sistemas-informaticos/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sel = scrapy.Selector(response)

        main_content = sel.xpath("//main")
        first_h3 = main_content.xpath(".//h3[1]/text()").get()
        if not first_h3:
            self.log("No H3 found under <main>.")
            return

        first_h3 = first_h3.strip()

        # Extract metadata
        page_title = response.xpath("//title/text()").get().strip()
        url = response.url
        extracted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        md_content = f"---\n"
        md_content += f"title: {page_title}\n"
        md_content += f"url: {url}\n"
        md_content += f"extracted: {extracted_date}\n"
        md_content += f"---\n\n"

        md_content += f"# {first_h3}\n\n"

        # Find all elements with the class "t3ddy-item t3ddy-tab-item"
        tab_items = sel.css(".t3ddy-item.t3ddy-tab-item")

        for tab_item in tab_items:
            # Extract all text content within the tab item
            text_content = tab_item.xpath(".//text()[normalize-space()]").getall()
            for text in text_content:
                md_content += f"{text.strip()}\n\n"

        # Save the markdown content to a file in the "documents" folder
        output_dir = Path("documents")
        output_dir.mkdir(exist_ok=True)
        file_name = f"{first_h3.replace(' ', '_')}.md"
        output_path = output_dir / file_name
        output_path.write_text(md_content, encoding="utf-8")

        self.log(f"Markdown file saved: {output_path}")
