#!/usr/bin/env ruby
#The regular expression must be only matching: capital letters

if ARGV.length == 1
  puts ARGV[0].scan(/[A-Z]/).join("")
  exit
end
