defmodule Bob do
  def hey(input) do
    text = String.trim(input)
    yelling? = text == String.upcase(text) and text != String.downcase(text)
    q? = String.ends_with?(text, "?")

    case {text, yelling?, q?} do
      {"", _, _} -> "Fine. Be that way!"
      {_, true, true} -> "Calm down, I know what I'm doing!"
      {_, false, true} -> "Sure."
      {_, true, _} -> "Whoa, chill out!"
      _ -> "Whatever."
    end
  end
end
