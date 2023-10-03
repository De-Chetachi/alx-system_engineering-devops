#!/usr/bin/env ruby

if ARGV.length == 1
  puts ARGV[0].scan(/^[0-9]{10}$/).join("")
  exit
end
