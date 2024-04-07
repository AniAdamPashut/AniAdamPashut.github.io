let rec my_map transform xs =
    match xs with
    | [] -> []
    | y::ys -> transform y :: my_map transform ys
