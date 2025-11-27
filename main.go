package main

import (
	pb "agent/pb"
	_ "trpc.group/trpc-go/trpc-filter/debuglog"
	_ "trpc.group/trpc-go/trpc-filter/recovery"
	trpc "trpc.group/trpc-go/trpc-go"
	"trpc.group/trpc-go/trpc-go/log"
)

func main() {
	s := trpc.NewServer()
	impl := Impl{}
	// 和一般的 tRPC 服务注册是一致的
	pb.RegisterServiceService(s.Service("trpc.test.helloworld.GreeterHTTP"), &impl)
	if err := s.Serve(); err != nil {
		log.Fatal(err)
	}
}
