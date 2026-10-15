require "bibtex"

module Jekyll
  class PublicationYearsGenerator < Generator
    safe true
    priority :high

    def generate(site)
      bibliography_path = File.join(site.source, "_bibliography", "papers.bib")
      bibliography = BibTeX.open(bibliography_path)

      years = bibliography.each_entry.each_with_object([]) do |item, result|
        year = item[:year].to_s[/\d{4}/]
        result << year.to_i if year
      end

      site.data["publication_years"] = years.uniq.sort.reverse
    end
  end
end
