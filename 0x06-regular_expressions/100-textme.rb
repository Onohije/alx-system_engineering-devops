#!/usr/bin/env ruby
# Regular expression to find all occurrences of a pattern in the input that matches:
# [from:<anything>][to:<anything>][flags:<anything>] and then joins the matches with commas.
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
