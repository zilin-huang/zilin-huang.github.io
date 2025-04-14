require 'nokogiri'
require 'httparty'
require 'jekyll'
require 'date'

module ExternalPosts
  class ExternalPostsGenerator < Jekyll::Generator
    safe true
    priority :high

    def generate(site)
      if site.config['external_sources'] != nil
        site.config['external_sources'].each do |src|
          p "Fetching external posts from #{src['name']}:"
          xml = HTTParty.get(src['rss_url']).body
          doc = Nokogiri::XML(xml)
          
          doc.xpath('//item').each do |item|
            title = item.xpath('title').text
            url = item.xpath('link').text
            content = item.xpath('description').text
            published_str = item.xpath('pubDate').text
            
            # Parse the date string into a Time object
            published = DateTime.parse(published_str).to_time
            
            p "...fetching #{url}"
            slug = title.downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')
            path = site.in_source_dir("_posts/#{slug}.md")
            
            doc = Jekyll::Document.new(
              path, { :site => site, :collection => site.collections['posts'] }
            )
            
            doc.data['external_source'] = src['name']
            doc.data['feed_content'] = content
            doc.data['title'] = title
            doc.data['description'] = content
            doc.data['date'] = published
            doc.data['redirect'] = url
            
            site.collections['posts'].docs << doc
          end
        end
      end
    end
  end

end
