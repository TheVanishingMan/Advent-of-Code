#lang racket

;; Advent of Code
;; Alexander L. Hayes
;; Day 4

;; Problem 1: MD5 fun

(require file/md5)

(define check-hash
  (λ (str number)
    (let* ([num (number->string number)]
           [test (string-append str num)])
      (cond
        ((equal? (bytes->list (subbytes (md5 test) 0 5)) '(48 48 48 48 48)) (values (string->number num) test))
        (else (check-hash str (add1 number)))
        ))))

(define mine-coins ;; (mine-coins "abcdef")
  (λ (str)         ;; (mine-coins "ckczppom")
    (check-hash str 0)))


;; Problem 2: Now find one with 6 leading zeros

(define check-hash-6
  (λ (str number)
    (let* ([num (number->string number)]
           [test (string-append str num)])
      (cond
        ((equal? (bytes->list (subbytes (md5 test) 0 6)) '(48 48 48 48 48 48)) (values (string->number num) test))
        (else (check-hash-6 str (add1 number)))
        ))))

(define mine-coins-6 ;; finds a string that produces 6 leading zeros
  (λ (str)
    (check-hash-6 str 0)))

(define mine-coins-seed ;; finds the same thing, but specifies a number as a starting point
  (λ (str start)        ;; i.e. (mine-coins-seed "ckczppom" 100000)
    (check-hash-6 str start)))

;; Because I'm crazy and curious


(define check-hash-7 ;; (check-hash-7 "ckczppom" 0)
  (λ (str number)
    (let* ([num (number->string number)]
           [test (string-append str num)])
      (cond
        ((equal? number 5000000) (println "done"))
        ((equal? (bytes->list (subbytes (md5 test) 0 4)) '(48 48 48 48)) (and (println (number->string number)) (check-hash-7 str (add1 number)))) ;(values (string->number num) test (md5 test))))
        (else (check-hash-7 str (add1 number)))
        ))))

(define mine-coins-seed-7 ;; finds a string that produces 6 leading zeros
  (λ (str start)
    (check-hash-7 str start)))