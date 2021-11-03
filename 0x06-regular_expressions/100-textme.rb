#!/usr/bin/env ruby
s = ARGV[0]
puts "#{/\[from:(.*?)\]/.match(s).captures[0]},#{/\[to:(.*?)\]/.match(s).captures[0]},#{/\[flags:(.*?)\]/.match(s).captures[0]}"
