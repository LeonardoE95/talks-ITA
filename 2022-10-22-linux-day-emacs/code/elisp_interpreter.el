(defun my-eval (e a)
  (cond
   ((atom e) (cadr (assoc e a)))
   ((atom (car e))
    (cond
     ((eq (car e) 'quote) (cadr e))     
     ((eq (car e) 'atom) (atom (my-eval (cadr e) a)))
     ((eq (car e) 'eq) (eq (my-eval (cadr e) a)
			   (my-eval (caddr e) a)))
     ((eq (car e) 'car) (car (my-eval (cadr e) a)))
     ((eq (car e) 'cdr) (cdr (my-eval (cadr e) a)))
     ((eq (car e) 'cons) (cons (my-eval (cadr e) a)
			       (my-eval (caddr e) a)))
     ((eq (car e) 'cond) (my-evcon (cdr e) a))
     ('t
      (progn
	(my-eval (cons (cadr (assoc (car e) a))
		       (cdr e))
		 a)))))
   
   ((eq (caar e) 'lambda)    
    (my-eval (caddar e)
	  (append (my-pair (cadar e)
			(my-evlis (cdr e) a))
		  a)))))

(defun my-evcon (c a)
  (cond ((my-eval (caar c) a) (my-eval (cadar c) a))
	('t (my-evcon (cdr c) a))))

(defun my-evlis (m a)
  (cond ((null m) '())
	('t (cons (my-eval (car m) a)
		  (my-evlis (cdr m) a)))))

(defun my-pair (x y)
  (cond ((and (null x) (null y)) '())
	((and (not (atom x)) (not (atom y)))
	 (cons (list (car x) (car y))
	       (my-pair (cdr x) (cdr y))))))

;; ----------------------------------------------------------

(my-eval '((lambda (x) (cons '1 x)) a) '((a 2)))
