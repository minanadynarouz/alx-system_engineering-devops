#!/usr/bin/env ruby
# Match string literal "School"
puts ARGV[0].scan(/(?<=from:|to:|flags:).*?(?=])/).join(",")
