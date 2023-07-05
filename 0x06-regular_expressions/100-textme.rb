#!/usr/bin/env ruby

put ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
