func max(a, b int) int {
    if a > b{
        return a
    }
    return b
}

func minimumSemesters(n int, relations [][]int) int {
    pGraph := make(map[int][]int)
    inDegree := make(map[int]int)
    for _, coursePair := range relations {
        prereq := coursePair[0]
        course := coursePair[1]
        pGraph[prereq] = append(pGraph[prereq], course)
        inDegree[course] += 1
    }

    queue := [][]int{}
    for i:=0;i<n;i++ {
        if inDegree[i] == 0 {
            queue = append(queue, []int{i, 1}) 
        }
    }
    maxSemester := 0
    visited := make([]bool, n+1)
    for len(queue) > 0 {
        element := queue[0]
        queue = queue[1: len(queue)] //removing element from the queue
        course := element[0]
        visited[course] = true
        semester := element[1]
        maxSemester = max(maxSemester, semester)
        for _, dependentCourse := range pGraph[course] {
            inDegree[dependentCourse] -= 1
            if inDegree[dependentCourse] == 0 && !visited[dependentCourse]{
                visited[dependentCourse] = true
                queue = append(queue, []int{dependentCourse, semester+1})
            }
        }
    }

    for i:=1;i<n;i++ {
        if !visited[i] {
            return -1
        }
    }
    return maxSemester
}