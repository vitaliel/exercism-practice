defmodule RotationalCipher do
  @doc """
  Given a plaintext and amount to shift by, return a rotated string.

  Example:
  iex> RotationalCipher.rotate("Attack at dawn", 13)
  "Nggnpx ng qnja"
  """
  @spec rotate(text :: String.t(), shift :: integer) :: String.t()
  def rotate(text, shift) do
    result = for <<ch <- text>>, do: encode(ch, shift)
    List.to_string(result)
  end

  defp encode(char, shift) when char in ?a..?z, do: adjust(char + shift, ?z)
  defp encode(char, shift) when char in ?A..?Z, do: adjust(char + shift, ?Z)
  defp encode(char, _shift), do: char

  defp adjust(char, limit) when char > limit, do: char - 26
  defp adjust(char, _limit), do: char
end
