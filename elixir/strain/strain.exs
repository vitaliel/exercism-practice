defmodule Strain do
  @doc """
  Given a `list` of items and a function `fun`, return the list of items where
  `fun` returns true.

  Do not use `Enum.filter`.
  """
  @spec keep(list :: list(any), fun :: (any -> boolean)) :: list(any)
  def keep(list, fun) do
    filter(list, fun, [])
  end

  @doc """
  Given a `list` of items and a function `fun`, return the list of items where
  `fun` returns false.

  Do not use `Enum.reject`.
  """
  @spec discard(list :: list(any), fun :: (any -> boolean)) :: list(any)
  def discard(list, fun) do
    reject(list, fun, [])
  end

  defp reject([], _, acc) do
    Enum.reverse(acc)
  end

  defp reject([head | tail], fun, acc) do
    if fun.(head) do
      reject(tail, fun, acc)
    else
      reject(tail, fun, [head | acc])
    end
  end

  defp filter([], _, acc) do
    Enum.reverse(acc)
  end

  defp filter([head | tail], fun, acc) do
    if fun.(head) do
      filter(tail, fun, [head | acc])
    else
      filter(tail, fun, acc)
    end
  end
end
