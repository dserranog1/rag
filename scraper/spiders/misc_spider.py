from pathlib import Path

import scrapy


class MiscSpider(scrapy.Spider):
    name = "misc"

    def start_requests(self):
        urls = [
            "https://manizales.unal.edu.co/menu/programas-academicos/carreras/",
            "https://manizales.unal.edu.co/menu/programas-academicos/posgrados/",
            "https://manizales.unal.edu.co/menu/institucional/naturaleza-fines-y-principios/",
            "https://manizales.unal.edu.co/menu/institucional/resena-historica/",
            "https://manizales.unal.edu.co/menu/institucional/dependencias-administrativas/"

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
        # page_title = response.xpath("//title/text()").get().strip()
        url = response.url
        # extracted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        md_content = f"---\n"
        md_content += f"url: {url}\n"
        # md_content += f"extracted: {extracted_date}\n"
        md_content += f"---\n\n"

        md_content += f"# {first_h3}\n\n"

        container_div = sel.xpath("//div[@id='columna1']")
        text_elements = container_div.xpath(
            ".//text()[normalize-space() and not(ancestor::h3)]"
        ).getall()
        for text in text_elements:
            md_content += f"{text.strip()}\n\n"
        # Save the markdown content to a file in the "documents" folder
        output_dir = Path("documents")
        output_dir.mkdir(exist_ok=True)
        file_name = f"{first_h3.replace(' ', '_')}.md"
        output_path = output_dir / file_name
        output_path.write_text(md_content, encoding="utf-8")

        self.log(f"Markdown file saved: {output_path}")
