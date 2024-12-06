package main

import (
	"fmt"
	"lr9/task_4/solution"
)

func main() {
	resp, err := solution.Solution()
	if err != nil {
		fmt.Printf("failed to get solution: %v\n", err)
		return
	}

	fmt.Printf("responsee is: %s\n", resp)
}
