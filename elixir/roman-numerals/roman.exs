defmodule Roman do
  @doc """
  Convert the number to a roman number.
  """
  @spec numerals(pos_integer) :: String.t()
  def numerals(number) do
    [u, z, s, m] = Integer.digits(number) |> Enum.reverse() |> make4digits

    romans =
      convert([], u, "I", "V", "X")
      |> convert(z, "X", "L", "C")
      |> convert(s, "C", "D", "M")
      |> convert(m, "M", "?", "?")

    Enum.join(romans, "")
  end

  defp convert(acc, digit, l, m, h) do
    ro =
      cond do
        digit in 0..3 -> String.duplicate(l, digit)
        digit == 4 -> "#{l}#{m}"
        digit in 5..8 -> "#{m}#{String.duplicate(l, digit - 5)}"
        digit == 9 -> "#{l}#{h}"
      end

    [ro | acc]
  end

  defp make4digits([u]), do: [u, 0, 0, 0]
  defp make4digits([u, z]), do: [u, z, 0, 0]
  defp make4digits([u, z, s]), do: [u, z, s, 0]
  defp make4digits([u, z, s, m | _]), do: [u, z, s, m]
end
