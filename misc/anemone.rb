#! /usr/bin/env ruby
require 'anemone'

Anemone.crawl("https://amnesia.cbrain.mcgill.ca/SIMON_data/SIMON_BIDS/") do |anemone|
  anemone.on_every_page do |page|
      puts page.url
  end
end
