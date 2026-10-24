# AI Decision Explainability & Human Override

كل اختيار آلي يجب أن يوضح `matched_signals`, `decision`, `reason`, `implementation_action`, وReview relationships.

الوكيل لا يخفي الالتباس. عند تساوي أدلة Composition أو تعارض Journey، يظهر Review.

التجاوز البشري مسموح إذا سُجل السبب وADR/Exception عند أثر معماري أو أمني، ولا يجوز للتجاوز تخفيف ضابط أمني إلزامي دون مسار استثناء رسمي.

لا تستخدم درجة ثقة رقمية وهمية إذا لم تكن مبنية على نموذج قابل للمعايرة. يكفي `selected / needs_review / not_selected / verify_first`.
