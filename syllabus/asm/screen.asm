	@pixel
	M=-1
	@16384   // screen
	D=A
	@pos
	M=D
	@8192
	D=A
	@count
	M=D
(LOOP)
	@pixel
	D=M
	@pos
	A=M
	M=D
	@pos
	M=M+1
	@count
	MD=M-1
	@LOOP
	D;JGT

