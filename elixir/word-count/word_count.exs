defmodule Words do
  @doc """
  Count the number of words in the sentence.

  Words are compared case-insensitively.
  """
  @spec count(String.t()) :: map
  def count(sentence) do
    words =
      sentence
      |> String.downcase()
      |> String.replace(~r/[^\w-]+/u, " ")
      |> String.replace("_", " ")
      |> String.trim()
      |> String.split(~r/\s+/)

    List.foldl(words, %{}, fn el, acc ->
      if Map.has_key?(acc, el) do
        Map.put(acc, el, acc[el] + 1)
      else
        Map.put(acc, el, 1)
      end
    end)
  end
end
