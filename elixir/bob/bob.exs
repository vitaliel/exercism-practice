# Ported my python solution https://exercism.io/tracks/python/exercises/bob/solutions/46b976ab3d844677b10dbe9f02fec1d9
defmodule Bob do
  def hey(input) do
    text = String.trim(input)
    is_yelling = text == String.upcase(text) and text != String.downcase(text)

    cond do
      text == "" ->
        "Fine. Be that way!"

      String.ends_with?(text, "?") ->
        if is_yelling do
          "Calm down, I know what I'm doing!"
        else
          "Sure."
        end

      is_yelling ->
        "Whoa, chill out!"

      true ->
        "Whatever."
    end
  end
end
