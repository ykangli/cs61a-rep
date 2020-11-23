(define (factorial x)
(cond
  ((= x 0) 1)
  (else (* x (factorial (- x 1))))
  )
)


(define (fib n)
    (if (<= 1)
        n
        (+ (fib (- n 1)) (fib (- n 2)))
        )
)

(define (my-append a b)
(if (null? a)
    b
    (cons (car a) (my-append (cdr a) b))
    )
)

; 5.3 Write a Scheme function that, when given a list, such as (1 2 3 4),
; duplicates every element in the list (i.e. (1 1 2 2 3 3 4 4))
(define (duplicate lst)
(if (null? lst)
    lst
    (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
    )
)

(define (insert element lst index)
(if (= index 0)
    (cons element lst)
    (cons (car lst) (insert element (cdr lst) (- index 1)))
    )
)