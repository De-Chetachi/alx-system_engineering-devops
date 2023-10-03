#!/usr/bin/env ruby
#The regular expression must match School
if ARGV.length == 1
  puts ARGV[0].scan(/School/).join("")
  exit
end
