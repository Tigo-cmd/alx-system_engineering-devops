#!/usr/bin/env ruby
first = ARGV[0].scan(/from:(.*?)\]/)
second = ARGV[0].scan(/to:(.*?)\]/)
third = ARGV[0].scan(/flags:(.*?)\]/)
puts [first, second, third].join(',')
