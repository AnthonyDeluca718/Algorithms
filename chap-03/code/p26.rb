# Strings are immutable in python so we are doing the problem in Ruby

def reverse(str, i, j)
  while i < j
    temp = str[i]
    str[i] = str[j]
    str[j] = temp
    i += 1
    j -= 1
  end
end

def rev_words(str)
  i = 0
  j = 0

  while(j < str.length)
    if str[j] == ' '
      reverse(str, i, j - 1)
      j += 1
      i = j
    elsif j == str.length - 1
      reverse(str, i, j)
      j += 1
    else
      j += 1
    end
  end

  reverse(str, 0, str.length - 1)
end

str = 'My name is Chris'
rev_words(str)
p str
