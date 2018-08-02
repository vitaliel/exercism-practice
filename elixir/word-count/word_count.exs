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
      Map.update(acc, el, 1, &(&1 + 1))
    end)
  end
end
