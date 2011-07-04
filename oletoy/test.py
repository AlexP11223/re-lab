#!/usr/bin/env python

import inflate, vsd, sys, gsf

def main():
	if len(sys.argv) > 1:
		fname = sys.argv[1]
		src = gsf.InputStdio(fname)
		buf = src.read(src.size())
		defbuf = inflate.deflate(buf)
		ptr = vsd.pointer()
		ptr.length = len(defbuf)
		ptr.offset = 0
		res = inflate.inflate(ptr,defbuf)[0:len(buf)]
		print 'Len: ',len(buf),len(defbuf),len(res)
		if buf == res:
			print 'Success'
		else:
			print 'Failure'
	else:
		print 'Usage: test.py <file_to_test>'

if __name__ == '__main__':
	main()