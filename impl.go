package main

import (
	"context"

	pb "agent/pb"
)

type Impl struct{}

func (i *Impl) Hello(ctx context.Context, req *pb.Request) (*pb.Response, error) {
	rsp := &pb.Response{
		Msg: "Hello ",
	}
	return rsp, nil
}
