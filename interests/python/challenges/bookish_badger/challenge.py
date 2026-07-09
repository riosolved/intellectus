"""
BOOKISH BADGER — the town library
Difficulty: medium | Topic: classes & instance state

STORY
-----
Badger runs the only library in town. Books live on the shelves until a
member checks one out; then the book is in that member's hands until they
bring it back. Members who return books late owe a small fee, and Badger
is tired of tracking all of this on paper. Build him a system.

YOUR TASK
---------
Write three classes in code.py:

1. Book
   - has a `title` (str) and an `author` (str).

2. Member
   - has a `name` (str)
   - tracks the books they currently have checked out
   - tracks the total late fees they owe
   - has a method `owes()` that returns their total fees (float)
   - a member may hold AT MOST 3 books at a time.

3. Library
   - starts with these books on its shelves:
       "The Salted Sea"        by "M. Walrus"
       "Roots and Squares"     by "P. Fect"
       "A History of Shelves"  by "I. K. Ea"
       "Burrow Engineering"    by "B. Adger"
       "Quiet Please"          by "Anonymous"
   - has a method `find(title)` that returns the Book with that title
     if it is on the shelves
   - has a method `check_out(book, member, day)`:
       * moves the book from the shelves into the member's hands
       * the book is due back 14 days later
       * raise a ValueError if the book is not on the shelves
       * raise a ValueError if the member already holds 3 books
   - has a method `check_in(book, member, day)`:
       * moves the book from the member back onto the shelves
       * if it comes back late, charge the member 0.25 per day late

Your main() must make these asserts pass:

    library = Library()
    alice = Member("Alice")

    book = library.find("The Salted Sea")
    library.check_out(book, alice, day=3)      # due back on day 17
    library.check_in(book, alice, day=20)      # 3 days late

    assert alice.owes() == 0.75, "3 days late at 0.25/day should be 0.75"

    # Returning on time costs nothing:
    book = library.find("Quiet Please")
    library.check_out(book, alice, day=21)     # due back on day 35
    library.check_in(book, alice, day=35)      # exactly on time

    assert alice.owes() == 0.75, "an on-time return should add no fee"

    # A second library must NOT share state with the first:
    other = Library()
    assert other.find("The Salted Sea") is not None, (
        "a brand-new library should have all five books on its shelves"
    )

Also demonstrate the 3-book limit: check out three books to one member,
then show that a fourth attempt raises a ValueError.

BACKGROUND — ideas you need, explained
--------------------------------------
None of this gives away the code; it's the thinking behind it.

* Days as plain integers. There are no real calendar dates here. "Day 3"
  is just the number 3. If something happens on day 3 and is due 14 days
  later, the due day is 3 + 14 = 17. That's the whole date system —
  addition. You will want to REMEMBER the due day somewhere when a book
  is checked out, so that check_in can compare against it later.

* "Days late" is a subtraction with a floor. Returned on day 20, due on
  day 17 → 20 - 17 = 3 days late. Returned on day 35, due on day 35 →
  0 days late. Returned EARLY gives a negative number — and a negative
  number of late days must count as 0, not as a refund. Python's built-in
  `max(a, b)` returns the larger of two values; think about what
  `max(0, something)` does to negative numbers.

* Moving vs copying. When a book is checked out it should exist in
  exactly ONE place: the member's hands, not the shelves. So check_out
  removes it from one collection and adds it to another — the same
  "item moves between containers" shape as the store/cart exercise
  (salty_walrus). Removing from a list: `list.remove(item)`. Removing
  from a dict: `del d[key]`.

* Instance state, not class state. This is THE lesson from salty_walrus:
  a mutable value ([] or {}) written at class level is shared by every
  instance of that class. The third assert exists purely to catch this —
  if two Library objects share one shelf, checking a book out of the
  first removes it from the second too. Every list/dict a class owns
  belongs in __init__ as `self.something = ...`.

* Raising errors on purpose. `raise ValueError("message")` stops the
  program with your message unless the caller catches it. To PROVE that
  an error is raised (for the 3-book limit demo) without crashing your
  script, wrap the failing call in try/except:

      try:
          ...the call that should fail...
          assert False, "expected a ValueError here"
      except ValueError:
          pass    # good — it refused, as designed

* Why 0.25 and not 0.10? Fractions like 0.1 can't be stored exactly in
  floating point, so `==` comparisons on them can fail in surprising
  ways. 0.25 and 0.75 are powers of two underneath, so they're exact and
  safe to compare with ==. (Real money code uses integer cents for this
  reason — worth remembering, not needed here.)

HINTS (nudges, not answers)
---------------------------
* Decide where each piece of state lives BEFORE coding: who knows the
  shelf contents? who knows the due day of a borrowed book? who knows
  the fees? Every bug in the store exercise came from state living in
  the wrong place (or being shared).
* check_out has two failure conditions. Check both BEFORE changing any
  state — never charge/move first and validate after (that was bug #6
  in the salty_walrus review).
* `find` needs to look through the shelved books and match on title.
  A plain loop is fine; a dict keyed by title is also fine.

When you're done, solve it in
interests/python/challenges/bookish_badger/code.py, run it with
`atk run` (once your run command is built), then review it with
`atk review` on the same file.
"""
